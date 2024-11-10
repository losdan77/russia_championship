<template>
    <div>
    <NavbarMain/>
    <RedactProfile/>    
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
