<template>
  <v-app id="inspire">
    <v-container grid-list-md text-xs-center v-for="(item) in desserts">
      <v-layout row wrap>
        <v-flex xs5>
          <v-card>
            <v-img id="product-img"
                   :src="item.img"
                   height="100%"
                   class="grey darken-4"
            ></v-img>
          </v-card>
        </v-flex>
        <v-flex xs7 pl-5 class="d-flex text-xs-left">
          <div class="product-summary">
            <h2 class="product-title">{{ item.name }}</h2>
            <div class="price">
              <h3>
                <span>$</span>
                {{ item.price }}
              </h3>
            </div>
            <div class="prodect-details">
              <h3 class="infoproduct">Thông tin sản phẩm</h3>
              <p class="detail">{{ item.detail }}</p>
            </div>
            <div>
              <ul class="quantity" id="col-box">
                <p class="infoproduct">Số lượng : </p>
                <v-text-field class="quantity_fill"
                              filled
                              label="SL"
                              v-model="cart.quantity"
                              required
                ></v-text-field>
              </ul>
            </div>
            <div>
              <ul class="size" id="size-box">
                <p class="infoproduct"> Chọn size : </p>
                <li class="size-box size-option" @click="cart.size = 'M'"
                    :style="`background-color: ${cart.size === 'M' ? '#B2DFDB' : 'white'}`">M
                </li>
                <li class="size-box size-option" @click="cart.size = 'L'"
                    :style="`background-color: ${cart.size === 'L' ? '#B2DFDB' : 'white'}`">L
                </li>
                <li class="size-box size-option" @click="cart.size = 'XL'"
                    :style="`background-color: ${cart.size === 'XL' ? '#B2DFDB' : 'white'}`">XL
                </li>
              </ul>
            </div>
            <div class="buy-product">
              <div class="cart-btn">
                <v-btn class="px-5" color="error" @click="openC(item.id)" v-if="isUser"><i
                    class="fa fa-shopping-cart"></i> THÊM VÀO GIỎ HÀNG
                </v-btn>
                <v-btn class="cart-btn px-5" color="error" v-if="isUser">MUA NGAY</v-btn>
              </div>
            </div>
          </div>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>
<script>
import Vue from 'vue'
import TopBar from "@/components/TopBar.vue";
import HelloWorld from "@/components/HelloWorld.vue";
import productItemUser from "@/components/productItemUser.vue";
import api from "@/plugins/url";

export default Vue.extend({
  name: 'Home',

  data: () => ({
    desserts: [],
    loading: false,
    selection: "col-6",
    size: [],
    cart: {
      size: 'M',
      product_id: null,
      quantity: null,
      is_hidden: 1,

    },
    isAdmin: localStorage.permission === 'admin',
    isUser: localStorage.permission === 'user',
    colorSizeHover: '#B2DFDB'
  }),
  methods: {
    async dessertsIt() {
      await api.get('/api/products/' + this.$route.params.id).then(response => {
        this.desserts = response.data
        console.log(this.$route.params.id)
      })
    },
    async openC(id) {
      this.cart.product_id = id
      await api.post('/api/carts', this.cart).then(response => {
        console.log(this.product)
      })
    }

  },
  beforeMount() {
    this.dessertsIt()
  }
})
</script>

<style scoped>
.body {
  padding: 35px 0px;
}

* {
  box-sizing: border-box;
  font-family: 'Lora', serif;

}

.product-img {
  cursor: pointer;
  margin-top: 10px;
}

.product-title {
  text-transform: uppercase;
  margin-bottom: 15px;
  font-size: 25px;
  line-height: 1.2em;
  font-family: 'Lora', serif;
}

.user-ratings {
  overflow: hidden;
  margin-bottom: 10px;
  margin-top: 5px;
  display: inline-block;
}

.star-rating {
  display: inline-block;
  font-size: 18px;
  position: relative;
  height: 18px;
  line-height: 18px;
  letter-spacing: 2px;
  width: 130px;
  font-family: FontAwesome;
}

.quantity_fill {
  width: 100px;
}

.star-rating:before {
  content: "\f005\f005\f005\f005\f123";
  position: absolute;
  top: 0;
  left: 0;
  color: #FC0;
  box-sizing: border-box;
}

.star-rating span {
  overflow: hidden;
  float: left;
  top: 0;
  left: 0;
  height: 18px;
  position: absolute;
  font-size: 0;
}

.user-ratings .total-review {
  vertical-align: middle;
  color: rgba(0, 0, 0, .5);
  box-sizing: border-box;
  float: right;
  font-size: 14px;
  text-decoration: none;
}

.total-review:hover {
  text-decoration: underline;
}

.price {
  display: block;
  margin-bottom: 10px;
  font-size: 20px;
}

.price h3 {
  display: inline-block;
  font-size: 28px;
  color: #E91E63;
}

.price del {
  padding: 0px 20px;
  font-size: 20px;
  color: #9E9E9E;
}

.prodect-details {
  padding-top: 15px;
  padding-bottom: 20px;
  font-family: 'Lora', serif;
  border-bottom: 1px dashed #ddd;
}

.col-box {
  height: 20px;
  width: 10px;
  font-weight: 400;

}

.colors {
  margin: 0px;
  padding: 0px;
  display: inline-block;
  margin-top: 20px;
  list-style: none;
}

.colors p {
  float: left;
  margin-top: 10px;
  color: #000;
  font-weight: 700;
  padding-right: 20px;
}

.color-box {
  height: 20px;
  margin: 5px;
  display: inline-block;
  cursor: pointer;
  opacity: 0.8
}

.active-col {
  outline: 1px dashed black;
}

.size {
  margin: 0px;
  padding: 0px;
  display: inline-block;
  margin-top: 20px;
  list-style: none;
}

.size p {
  float: left;
  margin-top: 10px;
  color: #000;
  font-weight: 700;
  padding-right: 38px;
}

.size-box {
  padding: 12px;
  margin: 0px 5px;
  display: inline-block;
  cursor: pointer;
  color: #000;
  font-weight: 400;

}

.active-siz {
  background-color: #B2DFDB;
}

.buy-product {
  margin-top: 15px;
  padding: 15px 0px;
  border-top: 1px dashed #ddd;

}

.product-qty {
  display: inline-block;
  margin-top: 20px;
  width: 100%;
}

.product-qty button.items-count {
  background-color: #fff;
  border: 1px #ddd solid;
  border-radius: 2px;
}

.product-qty button.items-count {
  font-size: 18px;
  line-height: 12px;
  height: 40px;
  width: 40px;
  color: #000;
}

.product-qty .qty {
  height: 40px;
  text-align: center;
  width: 70px;
  vertical-align: top;
  color: #000;
}

.qty {
  background-color: #ffffff;
  border: 1px #ced4da solid;
  border-radius: 2px;
  color: #666;
  font-size: 15px;
  font-weight: bold;
  margin: 0 -5px;
}

.sub-title {
  color: #000;
  font-weight: 700;
  padding-right: 38px;
}

.cart-btn {
  margin: 15px;
  border-bottom: 1px #e5e5e5 solid;
}

.cart-btn i {
  padding: 0px 10px;
}

.socal-link {
  margin: 0px;
  padding: 0px;
  margin-top: 20px;
  list-style: none;
  display: block;
}

.socal-link li {
  list-style: none;
  display: inline-block;
  margin: 0px 8px;
}

.socal-link li a {
  border: 1px #ddd solid;
  color: #666;
  font-size: 15px;
  line-height: 36px;
  padding: 8px 12px;
}

.socal-link li a:hover {
  background: #ff5252;
  color: #fff;
}

.quantity {
  font-size: 30px;
}

.activeimg {
  border: 1px solid #000;
}

.overview {
  margin-top: 30px;
}

.detail {
  font-size: 20px;
  font-weight: normal;
}

.size-option:hover {
  background-color: #B2DFDB;
}

.infoproduct {
  font-size: 25px;
}
</style>