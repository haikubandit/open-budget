// set base URL for application
const BASE_URL = 'http://127.0.0.1:5000/api';

/** processForm: get data from form and make AJAX call to our API. */

async function processGetRequest(evt) {
	const resp = await axios.get(`${BASE_URL}/2020`);

	console.log(resp.data);
}

$(document).ready(processGetRequest);
