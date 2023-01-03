<template>
  <v-card>
    <v-card-title>
      <span class="text-h5">Them san pham</span>
    </v-card-title>
    <v-card-text>
      <v-container v-for="(item) in desserts">
        <v-row>
          <v-col
              cols="5"
          >
            <v-text-field
                label="Ten san pham"
                v-model="item.name"
                required
            ></v-text-field>
          </v-col>
          <v-col
              cols="5"
          >
            <v-text-field
                label="Ma san pham"
                v-model="item.product_code"
                hint="Moi san pham co 1 ma khac nhau de dinh danh san pham"
            ></v-text-field>
          </v-col>
          <v-col cols="5">
            <v-text-field
                label="Hinh anh"
                v-model="item.img"
                required
            ></v-text-field>
          </v-col>
          <v-col cols="5">
            <v-text-field
                label="Gia"
                v-model="item.price"
                required
            ></v-text-field>
          </v-col>
          <v-col cols="10">
            <v-text-field
                label="Thong tin chi tiet san pham"
                v-model="item.detail"
                required
            ></v-text-field>
          </v-col>
          <v-col
              cols="5"
              sm="2.5"
          >
            <v-text-field
                v-model="item.brand_id"
                label="Thuong hieu"
                required
            ></v-text-field>

          </v-col>
          <v-col
              cols="5"
              sm="2.5"
          >
            <v-text-field
                v-model="item.category_id"
                label="The loai"
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
          @click="editItem"
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
    async dessertsIt() {
      await api.get('/api/products/' + this.$route.params.id).then(response => {
        this.desserts = response.data
        console.log(this.$route.params.id)
      })
    }
  },
  goToPage(path) {
    this.$router.push(path)
  },
}

</script>