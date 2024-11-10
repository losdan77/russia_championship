<template>
    <div>
        <NavbarMain/>
        <ViewProfile/>
    </div>
</template>

<script>
import NavbarMain from '../components/NavbarMain.vue'
import ViewProfile from '../components/ViewProfile.vue'

export default {
    data () {
        return {

        }
    },
    components : {
        NavbarMain,
        ViewProfile
    }
}
</script>
