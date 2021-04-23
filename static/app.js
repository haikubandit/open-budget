// set base URL for application
const BASE_URL = 'http://127.0.0.1:5000/api';

// let budgetDataResp;

// let budgetData = [];
let generalFundLabel = [];
let generalFundData = [];
let revenuesLabel = [];
let revenuesData = [];

// const budgetDataResp = function(data) {
// 	// name = data.name;
// 	console.log(data);

// 	return data;
// };

/** Get data from API */

async function processGetRequest() {
	const response = await axios(`${BASE_URL}/2020`)
		.then(response => {
			const data = response.data;
			console.log(data);
			return data;
		})
		.catch(err => {
			console.log('Error: ', err);
		});
	console.log(response);
	return response;
}

let budgetData = processGetRequest();

// let budgetData = budgetDataResp(
// 	axios
// 		.get(`${BASE_URL}/2020`)
// 		.then(response => {
// 			const data = response.data;
// 			console.log(data);
// 			return data;
// 		})
// 		.then(budgetDataResp)
// 		.catch(err => {
// 			console.log('Error: ', err);
// 		})
// );

console.log(budgetData);
console.log(budgetData.budgetData[0]);

/** Get General Fund Data and Labels for chart  **/

const budgetDataGeneralFund = budgetData.budgetData[0].general_fund;
console.log(budgetDataGeneralFund);
for (const lineItem in budgetDataGeneralFund) {
	// console.log(budgetDataGeneralFund[lineItem].budget);
	generalFundData.push(budgetDataGeneralFund[lineItem].budget);
	generalFundLabel.push(budgetDataGeneralFund[lineItem].dept);
}

/** Get Revenue Data and Labels for chart  **/

const budgetDataRevenues = budgetData.budgetData[1].revenues;
console.log(budgetDataRevenues);
for (const lineItem in budgetDataRevenues) {
	// console.log(budgetDataObj[lineItem].budget);
	revenuesData.push(budgetDataRevenues[lineItem].budget);
	revenuesLabel.push(budgetDataRevenues[lineItem].dept);
}

/** Create and render General Fund chart  **/

var ctxGeneralFund = document.getElementById('generalFundChart').getContext('2d');
var generalFundChart = new Chart(ctxGeneralFund, {
	type: 'bar',
	data: {
		// labels: [ 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange' ],
		labels: generalFundLabel,
		datasets: [
			{
				label: '2020 General Fund Appropriations',
				// data: [ 12, 19, 3, 5, 2, 3 ],
				data: generalFundData,
				backgroundColor: [
					'rgba(255, 99, 132, 0.2)',
					'rgba(54, 162, 235, 0.2)',
					'rgba(255, 206, 86, 0.2)',
					'rgba(75, 192, 192, 0.2)',
					'rgba(153, 102, 255, 0.2)',
					'rgba(255, 159, 64, 0.2)'
				],
				borderColor: [
					'rgba(255, 99, 132, 1)',
					'rgba(54, 162, 235, 1)',
					'rgba(255, 206, 86, 1)',
					'rgba(75, 192, 192, 1)',
					'rgba(153, 102, 255, 1)',
					'rgba(255, 159, 64, 1)'
				],
				borderWidth: 1
			}
		]
	},
	options: {
		title: {
			display: true,
			text: '2020 General Fund Appropriations test'
		},
		scales: {
			yAxes: {
				beginAtZero: true,
				ticks: {
					callback: function(value, index, values) {
						if (parseInt(value) >= 1000) {
							return '$' + value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
						} else {
							return '$' + value;
						}
					}
				}
			}
		}
	}
});

/** Create and render Revenues chart  **/

// var ctxRevenues = document.getElementById('revenuesChart').getContext('2d');
// var revenuesChart = new Chart(ctxRevenues, {
// 	type: 'doughnut',
// 	data: {
// 		// labels: [ 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange' ],
// 		labels: revenuesLabel,
// 		datasets: [
// 			{
// 				label: '2020 General Fund Appropriations',
// 				// data: [ 12, 19, 3, 5, 2, 3 ],
// 				data: revenuesData,
// 				backgroundColor: [
// 					'rgba(255, 99, 132, 0.2)',
// 					'rgba(54, 162, 235, 0.2)',
// 					'rgba(255, 206, 86, 0.2)',
// 					'rgba(75, 192, 192, 0.2)',
// 					'rgba(153, 102, 255, 0.2)',
// 					'rgba(255, 159, 64, 0.2)'
// 				],
// 				borderColor: [
// 					'rgba(255, 99, 132, 1)',
// 					'rgba(54, 162, 235, 1)',
// 					'rgba(255, 206, 86, 1)',
// 					'rgba(75, 192, 192, 1)',
// 					'rgba(153, 102, 255, 1)',
// 					'rgba(255, 159, 64, 1)'
// 				],
// 				borderWidth: 1
// 			}
// 		]
// 	},
// 	options: {
// 		title: {
//             display: true,
//             text: '2020 Revenue Streams'
//         },
// 		legend: {
// 			position: 'bottom'
// 		},
// 		scales: {
// 			yAxes: {
// 				beginAtZero: true,
// 				ticks: {
// 					callback: function(value, index, values) {
// 						if(parseInt(value) >= 1000){
// 						  return '$' + value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
// 						} else {
// 						  return '$' + value;
// 						}
// 					  }
// 				}
// 			}
// 		}
// 	}
// });
