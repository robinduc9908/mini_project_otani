<template lang="pug">
.home-page
  .header
    TopBar
  .content
    .category-clothes.mt-3(style="margin-top: 24px !important")
      h1.mt-3.pb-3.mx-5  Giỏ hàng
        Cart.px-2
</template>

<script>
  import Vue from 'vue'
  import HelloWorld from '../components/HelloWorld.vue'
  import productItem from "@/components/productItem.vue"
  import TopBar from "@/components/TopBar.vue";
  import api from "@/plugins/url";
  import Cart from "@/components/Cart.vue";
  export default Vue.extend({
    name: 'Home',

    components: {
      TopBar,
      Cart
    }})
</script>

<style scoped>

</style>