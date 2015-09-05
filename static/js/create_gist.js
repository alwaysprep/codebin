function slugify(text) {
  return text.toString().toLowerCase()
    .replace(/\s+/g, '-')           // Replace spaces with -
    .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
    .replace(/\-\-+/g, '-')         // Replace multiple - with single -
    .replace(/^-+/, '')             // Trim - from start of text
    .replace(/-+$/, '');            // Trim - from end of text
}


$("#a").click(function (e) {
  $(".settings").toggle("slow", function () {
    $(".settings").css({
      "background-color": "#2C3E50"
    });
    setTimeout(function () {
      $("#des").css({"display": "block"});
      $("#secim").css({"display": "block"});
      $(".secim").css({"display": "block"});
      $("#des").css({"display": "block"});
    }, 200);
  });
  e.stopPropagation()
});

$(document).click(function (e) {
  var container = $(".settings");
  if (!container.is(e.target) // if the target of the click isn't the container...
    && container.has(e.target).length === 0) // ... nor a descendant of the container
  {
    container.hide("slow");
  }
  e.stopPropagation()
});


$(document).ready(function () {
  $("#plus").on("click", function () {
    $("#input").show(1000);
    $(this).hide(1000);
  });

  $("#pluss").on("click", function () {
    $("#inputt").show(1000);
    $(this).hide(1000);
  });

  $("#form").on("submit", function (event) {
    if ($("#input").val().length >= 3) {
      event.preventDefault();
      $("#input").hide(1000);
      $("#plus").show(1000);
      $("#select").append("<option selected>" + $("#input").val() + "</option>");
      $("#selectt").html("<option></option>");

    }
    $("#input").val("");

  });

  $("#form").on("submit", function (event) {
    if ($("#inputt").val().length >= 3) {
      event.preventDefault();
      $("#inputt").hide(1000);
      $("#pluss").show(1000);
      $("#selectt").append("<option selected>" + $("#inputt").val() + "</option>");

    }
    $("#inputt").val("");
  });
});