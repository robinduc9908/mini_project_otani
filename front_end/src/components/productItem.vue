<template>
  <v-app>
    <div class="row">
      <div>
        <v-card class="mx-2 my-2" max-width="250">
          <template slot="progress">
            <v-progress-linear color="deep-purple" height="10" indeterminate></v-progress-linear>
          </template>

          <v-img height="200" :src="item.img"></v-img>

          <v-card-title>{{ item.name }}</v-card-title>
          <v-divider class="mx-4"></v-divider>

          <v-card-title>{{ item.price }}</v-card-title>


        </v-card>
      </div>
    </div>
  </v-app>
</template>


<script>
import api from "@/plugins/url";

export default {
  props: {
    item: {
      type: Object,
      required: true
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
@import "src/assets/main.scss";

::v-deep .v-application--wrap {
  min-height: unset !important;
}
</style>