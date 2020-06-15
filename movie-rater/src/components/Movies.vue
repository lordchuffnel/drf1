<template>
  <div class="layout">
    <div>
      <h3>List of Movies</h3>
      <MovieItem v-for="movie in movies" :key="movie.id" :movie="movie" @movie-clicked="movieClicked($event)" />
    </div>
    <MovieDetails :movie="selectedMovie" />
  </div>
</template>

<script>
import MovieItem from './MovieItem';
import MovieDetails from './MovieDetails';
export default {
  name: 'Movies',
  components: { MovieItem },
  data() {
    return {
      movies: [],
      selectedMovie: null,
    };
  },
  methods: {
    movieClicked(event) {
      this.selectedMovie = this.movies.find( movie => movie.id === event)
    }
  }
  created() {
    fetch('http://127.0.0.1:8000/api/movies/', {
      method: 'GET',
      headers: {
        Authorization: 'Token ', //find token from user
      },
    })
      .then((res) => res.json())
      .then((res) => (this.movies = res))
      .catch((err) => console.log(err));
  },
};
</script>

<style lang="stylus" scoped>
.layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
