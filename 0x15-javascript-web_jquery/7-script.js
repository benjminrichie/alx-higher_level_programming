$(document).ready(function () {
	$.getJSON(
		"https://swapi-api.alx-tools.com/api/people/5/?format=json",
		function (data) {
			$("DIV#character").text(data.name);
		}
	);
});

// OPTION 1
// $(document).ready(function () {
// 	$.getJSON(
// 		"https://swapi-api.alx-tools.com/api/people/5/?format=json",
// 		function (data) {
// 			$("DIV#character").text(data.name);
// 		}
// 	);
// });

// OPTION 2
// document.addEventListener("DOMContentLoaded", function () {
// 	fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json")
// 		.then((response) => response.json())
// 		.then((data) => {
// 			$("#character").text(data.name);
// 		});
// });
