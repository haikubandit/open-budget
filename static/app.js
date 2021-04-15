// set base URL for application
const BASE_URL = 'http://127.0.0.1:5000/api';

let generalFundResp = [];
let generalFundLabel = [];
let generalFundData = [];

/** processGetRequest: get data based on year making AJAX call to our API. */

async function processGetRequest() {
	const resp = await axios.get(`${BASE_URL}/2019`);

	console.log(resp.data);
	return resp.data;
}

// $(document).ready(processGetRequest);

generalFundResp = await processGetRequest();

console.log(generalFundResp);

// push general fund data into chart data and label arrays
for (const deptFund of generalFundResp.generalFundByDept) {
	generalFundData.push(deptFund.allocation);
	generalFundLabel.push(deptFund.dept);
}

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
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
		scales: {
			yAxes: {
				beginAtZero: true,
				ticks: {
					callback: function(value, index, values) {
						if(parseInt(value) >= 1000){
						  return '$' + value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
						} else {
						  return '$' + value;
						}
					  }
				}
			}
		}
	}
});
