<template>
  <div>
    <label for="title">Title</label><br/>
    <input placeholder="title" id='title' v-model="localMovie.title" /><br/>
    <label for="description">Description</label><br/>
    <textarea placeholder="description" id='description' v-model="localMovie.description" /><br/>
    <button @click='saveMovie()'>Save Movie</button>
  </div>
</template>

<script>
export default {
  name: 'MovieEdit',
  props: ['movie'],
  data() {
    return {
      localMovie: {...this.movie}
    }
  },
  watch: {
    movie: function(newVal, oldVal) {
      if(newVal !== oldVal) {
        this.localMovie = {...this.movie}
      }
    }
  },
  methods: {
    saveMovie() {
      console.log(movie.id)
    }
  }
}
</script>

<style scoped>

</style>