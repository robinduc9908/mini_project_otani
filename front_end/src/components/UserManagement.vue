<template>
  <v-card>
    <v-card-title>
      <v-spacer></v-spacer>
      <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
        :headers="headers"
        :items="desserts"
        :search="search"
    ></v-data-table>
  </v-card>
</template>
<script>
import api from "@/plugins/url";

export default {
  data: () => ({
    desserts: [],
    search: '',
  }),
  computed: {
    headers() {
      return [
        {text: "Id_user", value: 'id'},
        {text: "Name", value: 'name'},
        {text: "Phone", value: 'phone'},
        {text: "Email", value: 'email'},
        {text: "Address", value: 'address'},
        {text: "Permission", value: 'permission'},

      ]
    }
  },

  methods: {
    async dessertsIt() {
      await api.get('/api/users/').then(response => {
        this.desserts = response.data
      })
    },
    filterOnlyCapsText(value, search, item) {
      return value != null &&
          search != null &&
          typeof value === 'string' &&
          value.toString().toLocaleUpperCase().indexOf(search) !== -1
    }
  },
  beforeMount() {
    this.dessertsIt()
  },

}

</script>
<style rel="stylesheet/scss" lang="scss" scoped>
@import "src/assets/main.scss";

</style>
