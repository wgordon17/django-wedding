(function() {

	var arrow = document.getElementById("arrow");

	Velocity(arrow, {marginTop: ["-2%", "spring"]}, { duration: 1000, loop: true });

	arrow.addEventListener("click", scroll, false);
	arrow.addEventListener("touchstart", scroll, false);

	function scroll() {
		var banner = document.getElementById("banner-bg");
		Velocity(banner, "scroll", { duration: 1000 });
	}

	var day = document.getElementById("days"),
		hour = document.getElementById("hours"),
		min = document.getElementById("minutes");


	function adjust_date() {
		var day_arr = day.textContent.split(":"),
			hour_arr = hour.textContent.split(":"),
			min_arr = min.textContent.split(":");

		var day_str = day_arr[0],
			day_num = parseInt(day_arr[1]),
			hour_str = hour_arr[0],
			hour_num = parseInt(hour_arr[1]),
			min_str = min_arr[0],
			min_num = parseInt(min_arr[1]);

		if (min_num > 0) {
			min.textContent = min_str + ": " + (min_num - 1);
		} else {
			if (hour_num > 0) {
				min.textContent = min_str + ": " + 59;
				hour.textContent = hour_str + ": " + (hour_num - 1);
			} else {
				if (day_num > 0) {
					min.textContent = min_str + ": " + 59;
					hour.textContent = hour_str + ": " + 23;
					day.textContent = day_str + ": " + (day_num - 1);
				} else {
					day.style.display = "none";
					hour.style.display = "none";
					min.style.display = "none";
					var countdown = document.getElementById("countdown");
					countdown.appendChild(document.createTextNode("It is nigh!"));
					return;
				}
			}
		}
		setTimeout(adjust_date, 60 * 1000); // Every 60 seconds, adjust the date
	}

	setTimeout(adjust_date, 60 * 1000); // Every 60 seconds, adjust the date

	setTimeout(scroll, 2000); // Auto scroll after 2 seconds

}());