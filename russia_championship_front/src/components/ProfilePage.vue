<template>
    <div>
        <NavbarMain/>
        <div class="btn-line">
            <div class="btn-main" @click="goToInfo">
                На главную
            </div>
        </div>
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
    },
    methods: {
        goToInfo() {
            this.$router.push('/info')
        }
    }
}
</script>

<style scoped>
.btn-line {
    width:100%;
    height:15vh;
    display:flex;
    justify-content: end;
    align-items: end;
}

.btn-main {
    background-color: rgb(49,68,104);
    border: 1px solid #ddd;
    display:flex;
    justify-content: center;
    align-items: center;
    height:5vh;
    font-family: Golos-Text-Semibold;
    padding: 0 2vw;
    border-radius: 10px;
    margin-right:13vw;
    color:#fff;
}

.btn-main:hover {
    background-color: #ddd;
    cursor:pointer;
    color:#646464;
    transition: all .4s ease;
}
</style>
