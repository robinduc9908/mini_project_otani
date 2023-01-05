<template lang="pug">
.home-page
  .header
    TopBar
  .content
    .category-clothes.mt-3(style="margin-top: 24px !important")
      h1.mt-3.pb-3  Quần áo bóng đá
        br
        br
        v-btn(rounded='', color='primary', dark='', v-if="isAdmin").add_item(@click="addItem('/add')")  Thêm sản phẩm
        br
        v-row(style="margin-top: 24px !important")
          v-col(cols="3" v-for="(item, index) in desserts" :key="index")
            product-item-user.px-2(
              :item="item"
              @goToDetail="goToDetail"
              @onDelete="onDelete"
              @editItem="onEdit"
            )
    .category-shoes(style="margin-top: 24px !important")
      //h1 Giay the thao
    .category-sport(style="margin-top: 24px !important")
      //h1 Dung cu the thao
  .footer
</template>

<script>
  import Vue from 'vue'
  import HelloWorld from '../components/HelloWorld.vue'
  import productItem from "@/components/productItem.vue"
  import TopBar from "@/components/TopBar.vue";
  import api from "@/plugins/url";
  import productItemUser from "@/components/productItemUser.vue";

  export default Vue.extend({
    name: 'Home',

    components: {
      TopBar,
      HelloWorld,
      productItemUser
    },
    data: () => ({
    desserts: [],
    loading: false,
    selection: "col-6",
    isAdmin: localStorage.permission === 'admin',
    isUser: localStorage.permission === 'user',

  }),
  methods:{
    async dessertsIt() {
      await api.get('/api/products/category/1').then(response => {
        this.desserts = response.data
      })
    },
    async onDelete(id) {
      await this.dessertsIt()

    },
    addItem(path) {
      this.$router.push(path)
    },

    goToDetail(id) {
      this.$router.push({
        name: 'productitem',
        params: {
          id: id
        }
      })
    },
    onEdit(id) {
      this.$router.push({
        name: 'editItem',
        params: {
          id: id
        }
      })
    },

  },
  beforeMount() {
    this.dessertsIt()
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
