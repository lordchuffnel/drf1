<template>
  <div class="layout">
    <div>
      <MovieItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        @movie-clicked="movieClicked($event)"
        @movie-delete="movieDelete($event)"
        @movie-edit="movieEdit($event)"
      />
      <button @click='newMovie()'>New Movie</button>
    </div>
    <MovieDetails
      v-if="selectedMovie"
      :movie="selectedMovie"
      @update="update()"
    />
    <MovieEdit v-if="editedMovie" :movie="editedMovie" @update="update()"/>
  </div>
</template>

<script>
import MovieItem from './MovieItem';
import MovieDetails from './MovieDetails';
import MovieEdit from './MovieEdit';
export default {
  name: 'Movies',
  components: { MovieItem, MovieDetails, MovieEdit },
  data() {
    return {
      movies: [],
      selectedMovie: null,
      editedMovie: null,
    };
  },
  methods: {
    movieClicked(event) {
      this.editedMovie = null;
      this.selectedMovie = this.movies.find((movie) => movie.id === event);
    },
    movieEdit(event) {
      this.selectedMovie = null;
      this.editedMovie = this.movies.find((movie) => movie.id === event);
    },
    movieDelete(event) {
      fetch(`http://127.0.0.1:8000/api/movies/${event}/`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Token ', //find token from user
        },
      })
        .then(() => {
          this.movies = this.movies.filter((movie) => movie.id !== event);
        })
        .catch((err) => console.log(err));
    },
    update() {
      this.getMovies();
    },
    newMovie() {
      this.selectedMovie = null;
      this.editedMovie = {title: '', description: ''};
    },
    getMovies() {
      fetch('http://127.0.0.1:8000/api/movies/', {
        method: 'GET',
        headers: {
          Authorization: 'Token ', //find token from user
        },
      })
        .then((res) => res.json())
        .then((res) => {
          this.movies = res;
          if (this.selectedMovie) {
            this.selectedMovie = this.movies.find(
              (movie) => movie.id === this.selectedMovie.id
            );
          }
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getMovies();
  },
};
</script>

<style lang="stylus" scoped>
.layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
