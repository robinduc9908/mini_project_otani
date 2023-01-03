<template>
  <v-card>
    <v-card-title>
      <span class="text-h5">Thêm sản phẩm</span>
    </v-card-title>
    <v-card-text>
      <v-container>
        <v-row>
          <v-col
              cols="5"
          >
            <v-text-field
                label="Tên sản phẩm"
                v-model="product.name"
                required
            ></v-text-field>
          </v-col>
          <v-col
              cols="5"
          >
            <v-text-field
                label="Mã sản phẩm"
                v-model="product.product_code"
                hint="Moi san pham co 1 ma khac nhau de dinh danh san pham"
            ></v-text-field>
          </v-col>
          <v-col cols="5">
            <v-text-field
                label="Hình ảnh"
                v-model="product.img"
                required
            ></v-text-field>
          </v-col>
          <v-col cols="5">
            <v-text-field
                label="Giá"
                v-model="product.price"
                required
            ></v-text-field>
          </v-col>
          <v-col cols="10">
            <v-text-field
                label="Thông tin chi tiết sản phẩm"
                v-model="product.detail"
                required
            ></v-text-field>
          </v-col>
          <v-col
              cols="5"
              sm="2.5"
          >
            <v-text-field
                v-model="product.brand_id"
                label="Thương hiệu"
                required
            ></v-text-field>

          </v-col>
          <v-col
              cols="5"
              sm="2.5"
          >
            <v-text-field
                v-model="product.category_id"
                label="Thể loại"
                multiple
            ></v-text-field>
          </v-col>

        </v-row>
      </v-container>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
          color="blue darken-1"
          text
          @click="goToPage('/footballclothes')"
      >
        Close
      </v-btn>
      <v-btn
          color="blue darken-1"
          text
          @click="addItem"
      >
        Save
      </v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
import api from '../plugins/url'

export default {
  data() {
    return {
      product: {
        name: '',
        product_code: '',
        img: '',
        brand_id: '',
        category_id: '',
        is_hidden: 1,
        price: '',
        detail: ''
      }
    }
  },
  methods: {
    async addItem() {
      await api.post('/api/products', this.product).then(response => {
        console.log(this.product)

      })
    },
    goToPage(path) {
      this.$router.push(path)
    },
  }
}

</script>