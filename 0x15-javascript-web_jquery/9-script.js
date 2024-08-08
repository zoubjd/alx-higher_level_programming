$.ajax({
  type: 'POST',
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: (resource) => {
    $('DIV#hello').text(resource.hello);
  }
});
