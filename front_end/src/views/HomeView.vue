<template lang="pug">
.home-page
  .header
    TopBar
  .content
    .category-clothes.mt-3(style="margin-top: 24px !important")
      h1.mt-3.pb-3  Quần áo bóng đá
        v-row(style="margin-top: 24px !important")
          v-col(cols="3" v-for="(item, index) in desserts1" :key="index")
            product-item.px-2(:item="item")
    .category-shoes(style="margin-top: 24px !important")
      h1.mt-3.pb-3  Giày thể thao
        v-row(style="margin-top: 24px !important")
          v-col(cols="3" v-for="(item, index) in desserts2" :key="index")
            product-item.px-2(:item="item")
    .category-sport(style="margin-top: 24px !important")
      h1.mt-3.pb-3  Dụng cụ thể thao
        v-row(style="margin-top: 24px !important")
          v-col(cols="3" v-for="(item, index) in desserts3" :key="index")
            product-item.px-2(:item="item")

      //h1 Dung cu the thao
  .footer
</template>

<script>
  import Vue from 'vue'
  import HelloWorld from '../components/HelloWorld.vue'
  import productItem from "@/components/productItem.vue"
  import TopBar from "@/components/TopBar.vue";
  import api from "@/plugins/url";

  export default Vue.extend({
    name: 'Home',

    components: {
      TopBar,
      HelloWorld,
      productItem
    },
    data: () => ({
    desserts1: [],
    desserts2: [],
    desserts3: [],
    loading: false,
    selection: "col-6",

  }),
  methods: {
    async dessertsIt1() {
      await api.get('/api/products/category/4/1').then(response => {
        this.desserts1 = response.data
      })
    },
    async dessertsIt2() {
      await api.get('/api/products/category/4/2').then(response => {
        this.desserts2 = response.data
      })

    },
    async dessertsIt3() {
      await api.get('/api/products/category/4/3').then(response => {
        this.desserts3 = response.data
      })
    }
  },
  beforeMount() {
    this.dessertsIt1()
    this.dessertsIt2()
    this.dessertsIt3()

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
