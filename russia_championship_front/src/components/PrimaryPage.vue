<template>
    <div>
        <NavbarPrimary
            v-if="!isAuth"

        />
        <NavbarMain
            v-if="isAuth"
            @LogoutNav="logout" 
        />
    </div>
</template>

<script>
import NavbarPrimary from '..//components/NavbarPrimary.vue'
import NavbarMain from './NavbarMain.vue';
import axios from 'axios';

export default {
    data(){
        return{
            isAuth : false
        }
    },
    components : {
        NavbarPrimary,
        NavbarMain
    },
    methods : {
        logout(){
            this.isAuth = false
        }
    },
    async mounted(){
        const response = await axios.get('/api/user/me')
        if (response.data) {
            this.isAuth = true
        }
        console.log(response);
        
    }
}
</script>
