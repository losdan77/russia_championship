<template>
    <div>
    <NavbarMain/>
    <div class="redact-box">
        <RedactProfile/>
    </div>    
    </div>
</template>

<script>
import NavbarMain from '../components/NavbarMain.vue'
import RedactProfile from '../components/RedactProfile.vue'

export default {
    data () {
        return {

        }
    },
    components : {
        NavbarMain,
        RedactProfile
    }
}

</script>

<style scoped>
    .redact-box {
        display:flex;
        justify-content: center;
        align-items: start;
        padding-top:4vh;
        height:150vh;
    }
</style>
