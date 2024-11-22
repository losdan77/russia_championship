<template>
    <div class="main-page">
        <NavbarMain/>
        <div class="main-box">
            <MultiNav/>
        </div>
    </div>
</template>

<script>
import NavbarMain from '../components/NavbarMain.vue'
import MultiNav from '../components/MultiNav.vue'

export default {
    data () {
        return {

        }
    },
    components : {
        NavbarMain,
        MultiNav
    }
}
</script>

<style scoped>
.main-page {
    width:100%;
    height:95vh;
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    gap:2vh;
}

.main-box {
    width:100%;
    height:85vh;
    margin-top:2vh;
}
</style>