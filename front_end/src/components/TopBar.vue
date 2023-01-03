<template>
  <v-app>
    <v-app-bar
        app
        absolute
        color="F8F8FF"
        light
        height="150px"
    >
      <v-row>

        <v-img
            class="avatar"
            :src="require('../assets/images/rbd.jpg')"
        ></v-img>
        <v-col>
          <v-toolbar-title class="rdb">RBD Sports</v-toolbar-title>
          <v-toolbar-title class="rdb2">Sự uy tín tạo nên chất lượng</v-toolbar-title>
        </v-col>
        <v-col cols="2" class="search">
          <v-text-field
              label="Search"
              prepend-icon="mdi-vuetify"
              variant="outlined"
          ></v-text-field>

        </v-col>
        <v-spacer></v-spacer>
        <v-col cols="2" class="hotline1">
          <p class="hl1">Hotline1</p>
          <p class="sdt1">0123456789 </p>
        </v-col>
        <v-col cols="2" class="hotline2">
          <p class="hl2">Hotline2</p>
          <p class="sdt2">0974561154</p>
        </v-col>
        <v-col cols="2" class="address">
          <v-row>
            <p>Cơ sở 1 : 234 Phạm Văn Đồng, Bắc Từ Liêm, Hà Nội</p>
          </v-row>
          <v-row>
            <p>Cơ sở 2 : 20 Bạch Mai, Hai Bà Trưng, Hà Nội</p>
          </v-row>
        </v-col>
      </v-row>

    </v-app-bar>
    <div>

      <nav class='nav'>
        <div class='menu-item' @click="goToPage('//')"><a class='text' href='#'>Trang chủ</a></div>
        <div class='menu-item' @click="goToPage('/footballclothes')"><a class='text' href='#'>Quần áo bóng đá</a></div>
        <div class='menu-item' @click="goToPage('/footballshoes')"><a class='text' href='#'>Giày thể thao</a></div>
        <div class='menu-item' @click="goToPage('/sportequipment')"><a class='text' href='#'>Dụng cụ thể thao</a></div>
        <div v-if="isAdmin" class='menu-item' @click="goToPage('/user')"><a class='text' href='#'>Quản lý người dùng</a>
        </div>
        <div v-if="isUser" class='menu-item' @click="goToPage('/cartview')"><a class='text' href='#'>Giỏ Hàng</a></div>
      </nav>

    </div>
    <div>
      <v-carousel>
        <v-carousel-item class="caroulsel"
                         v-for="(item,i) in items"
                         :key="i"
                         :src="item.src"
                         reverse-transition="fade-transition"
                         transition="fade-transition"
        ></v-carousel-item>
      </v-carousel>
    </div>
  </v-app>

</template>

<script>

export default {
  data() {
    return {
      isAdmin: localStorage.permission === 'admin',
      isUser: localStorage.permission === 'user',

      items: [
        {
          src: "https://iweb.tatthanh.com.vn/pic/12/banner/163561683_876278912934832_7497640669404054062_o.jpg.png",
        },
        {
          src: "https://iweb.tatthanh.com.vn/pic/12/banner/back to school.jpg",
        },
        {
          src: "https://iweb.tatthanh.com.vn/pic/12/banner/banner giày.jpg",
        },
        {
          src: "https://iweb.tatthanh.com.vn/pic/12/banner/8272af7461c1a79ffed0 (1).jpg",
        },
      ],
    }
  },
  methods: {
    goToPage(path) {
      this.$router.push(path)
    },
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
@import "src/assets/main.scss";

::v-deep .v-application--wrap {
  min-height: unset !important;
}
</style>