<template>
    <div>
        <div class="row post" v-for="post in posts">
            <div class="col-11" >
                <p>Role: {{ post.text }}</p>
                <p>Punishment: {{ post.punishment_quantity }} {{ post.punishment_type }}</p>
                <p>Author: {{ post.author.username }}</p>
            </div>
            <PunishmentCount v-bind:count="post.punishment_count"
                             v-bind:post_id="post.id"
                             v-bind:punishment_quantity="post.punishment_quantity"
            />
            <div class="line"></div>
        </div>

    </div>
</template>

<script>
import PunishmentCount from '@/components/PunishmentCount.vue'

export default {
    name: "Content",
    props: {
        posts: ""
    },
    components: {
        PunishmentCount
    }
}
</script>

<style scoped>

</style>