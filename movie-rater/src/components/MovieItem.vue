<template>
  <div>
    <h2 @click="$emit('movie-clicked', movie.id)">{{ movie.title }}</h2>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: ['movie'],
};
</script>
