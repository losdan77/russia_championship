<template>
    <div class="main-page">
        <NavbarMain/>
    </div>
</template>

<script>
import NavbarMain from '../components/NavbarMain.vue'

export default {
    data () {
        return {

        }
    },
    components : {
        NavbarMain,
    }
}
</script>

<style scoped>
.main-page {
    width:100%;
    height:100%;
}
</style>