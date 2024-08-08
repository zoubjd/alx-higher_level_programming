$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (movies) => {
    for (let i = 0; i < movies.results.length; i++) {
      $('UL#list_movies').append('<li>' + movies.results[i].title + '</li>');
    }
  }
});
