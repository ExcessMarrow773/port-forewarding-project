//const api_url = "http://10.28.247.226:5000/";
const api_url = "http://127.0.0.1:5000/";
async function getDate() {
	let api = api_url + "date";
	// Making an API call (request)
	// and getting the response back
	const response = await fetch(api);

	// Parsing it to JSON format
	const data = await response.json();
	console.log(data);

	// Retrieving data from JSON
	let date = data.date;

	document.title = date;

	// accessing the span container
	document.querySelector("#date").textContent = date;

}

async function getUser() {
	let api = api_url + "users";

	const response = await fetch(api)

	const data = await response.json();
	console.log(data.users[0]);


	document.querySelector("#users").textContent = data.users[0].name;
}

async function postTest() {
	let api = api_url + "post";

	const data = {
		key1: "value1",
		key2: "value2"
	};

	fetch(api, {method: "POST", headers: {'Content-Type': 'application/json'}, body: JSON.stringify(data)})
	.then(response => {
		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}
		return response.json(); // Parse the JSON response
	})
	.then(result => {
		console.log('Success:', result);
	})
	.catch(error => {
		console.error('Error:', error);
	});
}

async function postUser() {
	let api = api_url + "postUser";

        const nameBox = document.getElementById("name");

	const data = {
		name: nameBox.value,
	};

	fetch(api, {method: "POST", headers: {'Content-Type': 'application/json'}, body: JSON.stringify(data)})
	.then(response => {
		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}
		return response.json(); // Parse the JSON response
	})
	.then(result => {
		console.log('Success:', result);
	})
	.catch(error => {
		console.error('Error:', error);
	});
}

//setInterval(getDate, 1000);
getUser();
