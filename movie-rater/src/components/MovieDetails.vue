<template>
  <div v-if='movie'>
    <h2>{{ movie.title }}</h2>
    <p>{{movie.description}}</p>
    <font-awesome-icon icon="star" :class=[movie.avg_rating > 0 ? 'orange' : ''] /> 
    <font-awesome-icon icon="star" :class=[movie.avg_rating > 1 ? 'orange' : ''] /> 
    <font-awesome-icon icon="star" :class=[movie.avg_rating > 2 ? 'orange' : ''] /> 
    <font-awesome-icon icon="star" :class=[movie.avg_rating > 3 ? 'orange' : ''] /> 
    <font-awesome-icon icon="star" :class=[movie.avg_rating > 4 ? 'orange' : ''] /> 
      ({{ movie.no_of_ratings }})
  </div>
</template>

<script>
export default {
  name: 'MovieDetails',
  props: ['movie'],
};
</script>

<style scoped>
.orange {
  color: orange;
}
</style>