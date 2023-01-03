<template>
  <v-container class="grey lighten-5">
    <v-row
        class="mb-6"
        no-gutters
    >
      <v-col>
        <div class="item">Sản phẩm</div>
      </v-col>
      <v-spacer></v-spacer>
      <v-col>
        <div class="item">Hình ảnh</div>
      </v-col>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>

      <v-col>
        <div class="item">Cỡ</div>
      </v-col>
      <v-col>
        <div class="item">Đơn giá</div>
      </v-col>
      <v-col>
        <div class="item">SL</div>
      </v-col>
      <v-col>
        <div class="item">Thành tiền</div>
      </v-col>
      <v-col>
        <div class="item">Thao tác</div>
      </v-col>
    </v-row>
    <br><br>
    <v-row
        class="mb-6"
        no-gutters
        v-for="(item, index) in desserts"
    >
      <v-col>
        <div class="cart_item">{{ item.name }}</div>
      </v-col>
      <v-spacer></v-spacer>
      <v-col>
        <v-img max-height="150" max-width="250" class="grey lighten-2 Card" :src="item.img"></v-img>
      </v-col>
      <v-spacer></v-spacer>
      <v-col>
        <div class="cart_item">{{ item.size }}</div>
      </v-col>
      <v-col>
        <div class="cart_item">{{ item.price }}</div>
      </v-col>
      <v-col>
        <div class="cart_item">{{ item.quantity }}</div>
      </v-col>
      <v-col>
        <div class="cart_item">{{ item.price * item.quantity }}</div>
      </v-col>
      <v-col>
        <v-btn depressed color="red" outlined @click="deleteItem(item.id)" class="delete-btn"> Xóa</v-btn>
      </v-col>
    </v-row>
    <br><br>

  </v-container>
</template>
<script>
import api from "@/plugins/url";
import Vue from "vue";

export default Vue.extend({

  data: () => ({
    desserts: [],
    loading: false,
    selection: "col-6",

  }),
  methods: {
    async dessertsIt() {
      await api.get('/api/carts').then(response => {
        this.desserts = response.data
        console.log(3333, this.desserts)
      })
    },
    async deleteItem(id) {
      await api.delete('/api/carts/' + id).then(response => {
        this.dessertsIt()

        console.log(id)

      })
    }
  },
  beforeMount() {
    this.dessertsIt()
  }
})

</script>
<style>
.delete-btn {
  margin-left: 10px;
  color: red !important;
  min-width: 84px;
}

.cart_item {
  font-size: medium;
  font-weight: bold;
  color: #666666;

}

.item {
  font-size: 20px;
}
</style>