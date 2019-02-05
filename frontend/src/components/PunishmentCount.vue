<template>
    <div class="col-1 punishment-count">
        <div @mouseover="showPlus" v-if="show" v-model="count">{{count}}</div>
        <div @mouseleave="showPlus" v-else >
            <font-awesome-icon @click="punishmentUp" class="plus" icon="plus" />
            <font-awesome-icon @click="punishmentDown" class="minus" icon="minus" />
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
        postId: "",
        punishment_quantity: ""
    },
    methods: {
        showPlus: function () {
            this.show = !this.show;
        },

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

.plus {
    font-size: 0.4em;
    display: inline;
    margin-right: 10%;
}

.minus {
    font-size: 0.4em;
    display: inline;
}
</style>