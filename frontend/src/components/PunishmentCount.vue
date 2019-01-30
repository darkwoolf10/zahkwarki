<template>
    <div class="col-1 punishment-count">
        <div @mouseover="showPlus" @click="punishmentUp" v-if="show">{{count}}</div>
        <div @mouseleave="showPlus" v-else class="plus">
            <font-awesome-icon icon="plus" />
        </div>
    </div>
</template>
<script>
const axios = require('axios');

export default {
    name: "PunishmentCount",
    data: function() {
         return  {
           show: true
         }
    },
    props: {
        count: "",
        post_id: "",
        punishment_quantity: ""
    },
    methods: {
        showPlus: function () {
            this.show = !this.show;
        },
        punishmentUp: function () {
           axios.post(this.$store.state.url_server + 'api/post_up/' + post_id,{
               headers: {'Authorization':'Token ' + sessionStorage.getItem("token")}
           })
           .then(function (response) {
             // handle success;
               this.count += this.punishment_quantity;
           })
           .catch(function (error) {
             // handle error
             console.log(error);
           });
        }
    }
}
</script>
<style lang="scss">
.punishment-count {
    float: left;
    font-size: 6em;
    text-align: center;
}

.punishment-count:hover {
    cursor: pointer;
}
</style>