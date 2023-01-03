<template lang="pug">
.home-page
  .header
    TopBar
  .content
    .userManagement.mt-3(style="margin-top: 24px !important")
      h1.mt-3.pb-3  Quản lý người dùng
        br
        br
        UserManagement

  .footer
</template>

<script>
  import Vue from 'vue'
  import UserManagement from "@/components/UserManagement.vue";
  import productItem from "@/components/productItem.vue"
  import TopBar from "@/components/TopBar.vue";
  import api from "@/plugins/url";

  export default Vue.extend({
    name: 'Home',

    components: {
      TopBar,
      UserManagement,

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