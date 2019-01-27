<template>
    <nav id="sidebar">
        <div class="sidebar-header">
            <h3>Zahkwarki</h3>
        </div>
        <ul class="list-unstyled components">
            <p>Pasha Fudko</p>
            <li class="">
                <a href="/">Home</a>
            </li>
            <li>
                <a href="/about">About</a>
            </li>
            <li>
                <a href="#pageSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">Pages</a>
                <ul class="collapse list-unstyled" id="pageSubmenu">
                    <li>
                        <a href="/codex">Zahkwar codex</a>
                    </li>
                    <li v-for="user in users">
                        <a href="#">{{ user.username }} punishment</a>
                    </li>
                </ul>
            </li>
        </ul>
    </nav>
</template>

<script>
    export default {
        name: "Sidebar",
        props: {
            users: ""
        }
    }
</script>

<style scoped>
    a {
        color: #fff;
    }
</style>