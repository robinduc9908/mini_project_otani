<template>
  <v-card class="mx-2 my-2" height="400" max-width="250">

    <div @click="goToDetail(item.id)">
      <v-img height="200" :src="item.img"></v-img>
      <div class="nameitem">{{ item.name }}</div>
      <v-divider class="mx-4"></v-divider>
      <div class="price">{{ item.price }}</div>
    </div>
    <div class="action" v-if="isAdmin">
      <v-btn depressed color="red" outlined @click="deleteItem(item.id)" class="delete-btn"> Xóa</v-btn>
      <v-btn depressed color="red" outlined @click="editItem(item.id)" class="edit-btn"> Sửa</v-btn>
    </div>

  </v-card>

</template>


<script>
import api from "@/plugins/url";

export default {
  data() {
    return {
      isAdmin: localStorage.permission === 'admin',
      isUser: localStorage.permission === 'user'
    }
  },
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  methods: {
    goToDetail(id) {
      this.$emit('goToDetail', id)
    },
    editItem(id) {
      this.$emit('edit', id)
      this.$router.push('/Add')

    },
    async deleteItem(id) {
      await api.delete('/api/products/' + id).then(response => {
        // this.$emit('onDelete',id)
        console.log(id)

      })
      console.log(3333)
      this.$emit('onDelete', id)
    }
  },

}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
@import "src/assets/main.scss";

::v-deep .v-application--wrap {
  min-height: unset !important;
}

.nameitem {
  padding: 10px 10px 10px 10px;
  font-size: 18px;
}

.price {
  padding: 10px 10px 10px 10px;
  font-size: 15px;
  color: gray;
}

.action {
  display: flex;
  justify-content: space-between;
  padding-left: 5px;
  padding-right: 15px;

  .delete-btn {
    margin-left: 10px;
    color: red !important;
    min-width: 84px;
  }

  .edit-btn {
    margin-left: 10px;
    color: green !important;
    min-width: 84px;
  }
}
</style>