var editor = ace.edit("editor");
editor.setTheme("ace/theme/" + $("#id_theme").val().toLowerCase());
editor.getSession().setMode("ace/mode/" + $("#id_language").val().toLowerCase());

$("#id_language").on("change", function () {
  editor.getSession().setMode("ace/mode/" + $("#id_language").val().toLowerCase());
});

$("#id_theme").on("change", function () {
  editor.setTheme("ace/theme/" + $("#id_theme").val().toLowerCase());
});

$("#editor").keyup(function (e) {
  $("#editorr").val(editor.getSession().getValue());
});

$("#select").on("change", function () {
  window.location.href = "/gist/" + slugify($("#select").val());
});

$("#selectt").on("change", function () {
  window.location.href = "/gist/" + slugify($("#select").val()) + "/" + slugify($("#selectt").val());
});

if ($(".errors p").length) {
  $("#myModal").modal('show')
}
