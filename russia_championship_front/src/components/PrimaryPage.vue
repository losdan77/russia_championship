<template>
    <div class="main-page">
        <NavbarPrimary/>
        <div class="main-box">
            <MultiNavPrimary/>
        </div>
    </div>
</template>

<script>
import NavbarPrimary from '../components/NavbarPrimary.vue'
import MultiNavPrimary from '../components/MultiNavPrimary.vue'

export default {
    data () {
        return {

        }
    },
    components : {
        NavbarPrimary,
        MultiNavPrimary
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