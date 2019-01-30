<template>
    <div class="text-center" id="form_login">
    <form class="form-signin">
      <img src="../../public/img/icons/iconfinder_Spell_Book_2913104.svg" alt="" width="256" height="256" />
      <div v-if="errors.length">
        <b>Пожалуйста исправьте указанные ошибки:</b>
        <ul>
          <li v-for="error in errors">{{ error }}</li>
        </ul>
      </div>
      <h1 class="h3 mb-3 font-weight-normal" v-else>Please sign in</h1>
      <label for="login" class="sr-only">Username</label>
      <input type="text" value="" id="login" class="form-control" placeholder="Username" v-model="user.username" required autofocus>
      <label for="password" class="sr-only">Password</label>
      <input type="password" value="" id="password" class="form-control my-2" placeholder="Password" v-model="user.password" required>
      <!--<div class="checkbox mb-3">-->
        <!--<label>-->
          <!--<input type="checkbox" value="remember-me"> Remember me-->
        <!--</label>-->
      <!--</div>-->
      <button class="btn btn-lg btn-info btn-block" type="button" @click="setLogin">Sign in</button>
    </form>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                user: {
                    username: "",
                    password: ""
                },
                errors: []
            }
        },
        methods: {
            setLogin(e) {
                if (this.user.username &&  this.user.password) {
                    $.ajax({
                        url: 'http://127.0.0.1:5000/api/login',
                        type: 'POST',
                        data: {
                            username: this.user.username,
                            password: this.user.password
                        },
                        success: (response) => {
                            sessionStorage.setItem("token", response.token);
                            this.$router.push({name: "home"});
                        }
                    })
                }
                this.errors = [];
                if (!this.user.username) {
                    this.errors.push('You must enter a username, or you did not enter it correctly.');
                }
                if (!this.user.password) {
                    this.errors.push('You must enter a password,  or you did not enter it correctly.');
                }

                e.preventDefault();
            }
        }
    }
</script>

<style scoped>
html,
body {
  height: 100%;
}
#form_login {
  margin-top: 10%;
}

body {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}
.form-signin .checkbox {
  font-weight: 400;
}
.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
.bd-placeholder-img {
    font-size: 1.125rem;
    text-anchor: middle;
}

@media (min-width: 768px) {
    .bd-placeholder-img-lg {
      font-size: 3.5rem;
    }
}
</style>