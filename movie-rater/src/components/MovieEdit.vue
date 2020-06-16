<template>
  <div>
    <label for="title">Title</label><br />
    <input placeholder="title" id="title" v-model="localMovie.title" /><br />
    <label for="description">Description</label><br />
    <textarea
      placeholder="description"
      id="description"
      v-model="localMovie.description"
    /><br />
    <button @click="saveMovie()">Save Movie</button>
  </div>
</template>

<script>
export default {
  name: 'MovieEdit',
  props: ['movie'],
  data() {
    return {
      localMovie: { ...this.movie },
    };
  },
  watch: {
    movie: function(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.localMovie = { ...this.movie };
      }
    },
  },
  methods: {
    saveMovie() {
      if (this.movie.id) {
        fetch(`http://127.0.0.1:8000/api/movies/${this.movie.id}/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
            Authorization: 'Token ', //find token from user
          },
          body: JSON.stringify({
            title: this.localMovie.title,
            description: this.localMovie.description,
          }),
        })
          .then((res) => res.json())
          .then(() => {
            this.$emit('update');
          })
          .catch((err) => console.log(err));
      } else {
                fetch(`http://127.0.0.1:8000/api/movies/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: 'Token ', //find token from user
          },
          body: JSON.stringify({
            title: this.localMovie.title,
            description: this.localMovie.description,
          }),
        })
          .then((res) => res.json())
          .then(() => {
            this.$emit('update');
          })
          .catch((err) => console.log(err));
      }
    },
  },
};
</script>

<style scoped></style>
