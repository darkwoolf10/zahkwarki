<template>
    <div>
        <input type="text" value="" placeholder="login" v-model="user.username">
        <input type="password" value="" placeholder="password" v-model="user.password">
        <button type="button" @click="setLogin">Login</button>
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
                }
            }
        },
        methods: {
            setLogin() {
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
        }
    }
</script>

<style scoped>

</style>