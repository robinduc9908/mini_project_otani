<template>
  <v-app>
    <v-app-bar app dark color="blue">
      <v-toolbar-title>Wellcome to RBD SPORTS</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-form @submit.prevent="loginVue">
      <v-main>
        <v-card width="500" class="mx-auto mt-9">
          <v-card-title>Login</v-card-title>
          <v-card-text>
            <v-text-field label="Email" prepend-icon="mdi-account-circle" v-model="login.email" required/>
            <v-text-field
                label="Password"
                v-model="login.password"
                type="password"
                prepend-icon="mdi-lock"/>
          </v-card-text>
          <v-alert class="alert"
                   v-if="showAlert"
                   type="error"
          >
            Invalid Email or Password!
          </v-alert>
          <v-card-actions>
            <v-btn type="submit" @click="loginVue" color="info">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-main>
    </v-form>
  </v-app>
</template>
<script>

import api from '../plugins/url'

export default {
  data() {
    return {
      login: {
        email: '',
        password: ''
      },
      showAlert: false,
      error: ''
    }
  },
  methods: {
    async loginVue() {
      try {
        await api.post('/api/users/login', this.login).then(response => {
          if (response.data.code === 200) {
            localStorage.name = response.data.data[0].username
            localStorage.email = response.data.data[0].email
            localStorage.permission = response.data.data[0].permission
            localStorage.phone = response.data.data[0].phone
            localStorage.id = response.data.data[0].id
            localStorage.password = response.data.data[0].password
            localStorage.address = response.data.data[0].address

            this.$router.push('/')

          } else {
            this.showAlert = true
            this.error = 'Invalid email/password!'
          }
        })
      } catch (e) {
        this.error = 'Invalid email/password!'

      }
    }
  }
}
</script>
