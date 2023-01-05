<template lang="pug">
.home-page
  .header
    TopBar
  .content
    .category-clothes.mt-3(style="margin-top: 24px !important")
      h1.mt-3.pb-3  Thong tin san pham
         product-detail.px-2
</template>

<script>
import {defineComponent, getCurrentInstance} from "vue";
import Vue from 'vue'
import HelloWorld from '../components/HelloWorld.vue'
import productItem from "@/components/productItem.vue"
import TopBar from "@/components/TopBar.vue";
import api from "@/plugins/url";
import productItemUser from "@/components/productItemUser.vue";
import productDetail from "@/components/productDetail.vue";

export default defineComponent({
      components: {
      TopBar,
      HelloWorld,
      productDetail
    },
  setup() {
    const instance = getCurrentInstance().proxy
    const {$route} = instance
  }
})
</script>
<style lang="scss" scoped>
.home-page{
  .content{
    max-width: 1000px;
    margin: auto;
  }
}
</style>
