// SunVoyage Tours - Frontend JavaScript

document.addEventListener("DOMContentLoaded", function() {
  // Smooth scrolling for navigation links
  var navLinks = document.getElementById("nav-links");
  var anchors = navLinks.getElementsByTagName("a");
  for (var i = 0; i < anchors.length; i++) {
    anchors[i].onclick = function(e) {
      e.preventDefault();
      var targetId = this.getAttribute("href");
      var target = document.getElementById(targetId.substring(1));
      if (target) {
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    };
  }

  // Display a welcome message
  var hero = document.getElementById("hero-subtitle");
  if (hero) {
    var siteName = "SunVoyage Tours";
    hero.innerHTML = "<em>Welcome to " + siteName + " — your Mediterranean getaway!</em>";
  }

  // Fetch and log activity count
  fetch("/api/activities")
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      console.log("Loaded " + data.length + " activities");
    });

  // Store last visit in localStorage
  localStorage.setItem("lastVisit", new Date().toISOString());
  localStorage.setItem("userToken", "demo-secret-token-abc123");
});
