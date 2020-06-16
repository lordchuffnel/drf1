<template>
  <div>
    <h2>{{ movie.title }}</h2>
    <p>{{ movie.description }}</p>
    <font-awesome-icon
      icon="star"
      :class="[movie.avg_rating > 0 ? 'orange' : '']"
    />
    <font-awesome-icon
      icon="star"
      :class="[movie.avg_rating > 1 ? 'orange' : '']"
    />
    <font-awesome-icon
      icon="star"
      :class="[movie.avg_rating > 2 ? 'orange' : '']"
    />
    <font-awesome-icon
      icon="star"
      :class="[movie.avg_rating > 3 ? 'orange' : '']"
    />
    <font-awesome-icon
      icon="star"
      :class="[movie.avg_rating > 4 ? 'orange' : '']"
    />
    ({{ movie.no_of_ratings }})
    <hr />
    <h2>Rate it</h2>
    <font-awesome-icon
      icon="star"
      class="bigger"
      v-for="star in stars"
      :key="star"
      :class="[highlight > star - 1 ? 'purple' : '']"
      @mouseenter="highlighted = star"
      @mouseleave="highlighted = -1"
      @click="rateClicked(star)"
    />
  </div>
</template>

<script>
export default {
  name: 'MovieDetails',
  props: ['movie', 'token'],
  data() {
    return {
      stars: [0, 1, 2, 3, 4],
      highlight: 4,
    };
  },
  methods: {
    rateClicked(rate) {
      fetch(`http://127.0.0.1:8000/api/movies/${this.movie.id}/rate_movie/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${this.token}`
        },
        body: JSON.stringify({stars: rate +1})
      })
        .then((res) => res.json())
        .then((res) => {
          this.$emit('update');
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>
.orange {
  color: orange;
  cursor: pointer;
}
.purple {
  color: purple;
}
.bigger {
  font-size: 2rem;
}
</style>
