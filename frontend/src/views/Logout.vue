<template>
  <div class="log">
    ASDASDASDASD
  </div>
</template>

<script>
  export default {
    created () {
      this.$store.dispatch('logoutUser')
        .then(() => {
          this.$router.push({ name: 'home' })
        })
    }
  }
</script>

<style scoped>
</style>
