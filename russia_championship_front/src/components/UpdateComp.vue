<template>
    <div class="text-box">
        <div class="text">Обновленные данные</div>
    </div>
    <div class="description-box">
        <div class="text-description">
            Отслеживайте последние изменения в списке событий. Вы можете просмотреть новые события и изменения информации в старых. 
        </div>
    </div>
    <div class="cards-box">
        <div class="card" v-for="(event,index) in events"
        :key="index"
        >
            <div class="line-one">
                <div class="box-id">
                    {{ event.id }}
                </div>
                <div class="line-group">
                <div class="box-date">
                    {{ event.start_date }} - {{ event.end_date }}
                </div>
                <div class="box-status">
                    Редактирован
                </div>
            </div>
            </div>
            <div class="line-one">
                <div class="box-name-sport">
                    {{event.name_sport}}
                </div>
                <div class="box-name-champ">
                    {{event.name_champ}}
                </div>
            </div>
            <div class="line-one">
                <div class="box-descriptions">
                    <!-- тут нужен for для decription -->
                    <div class="decription" v-for="(descrip,index) in event.description"
                    :key="index"
                    >
                        {{ descrip }}
                    </div>
                </div>
            </div>
            <div class="line-one">
                <div class="box-age-groups">
                    <!-- тут нужен for для age-group -->
                    <div class="age-group" v-for="(age,index) in event.age_group"
                    :key="index"
                    >
                        {{ age }}
                    </div>
                </div>
            </div>
            <div class="box-position">
                <div class="box-country">
                    {{event.country}}
                </div>
                <div class="box-subjetc">
                    {{ event.subjetc }}
                </div>
                <div class="box-city">
                    {{ event.city }}
                </div>
                <div class="box-count">
                    Количество участников: {{ event.number_of_participants }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
    export default {
        data() {
            return {
                events : []
            };
        },
        methods: {
            async searcJson(){
                try {
                    const response = await axios.get('../../public/updated.json');
                    console.log(response.data);
                    this.events = response.data
                } catch (error) {
                    console.log(error);
                    
                }

            }    
        },
        async mounted(){
            this.searcJson()
        }
    };
</script>

<style scoped>
.text-box {
    width:100%;
    height:10%;
    display:flex;
    justify-content: start;
    align-items: center;
}
.text {
    font-family:Golos-Text-Semibold;
    font-size:4vh;
}

.cards-box {
    width:100%;
    height:70%;
    overflow-y:scroll;
    overflow-x: hidden;
    display: flex;
    flex-direction: column;
    gap:.3vh;
}



.description-box {
    width:100%;
    height:5%;
    display:flex;
    justify-content: start;
    align-items: start;
}

.text-description {
    font-family:Golos-Text;
    font-size:2vh;
}

.card {
    width:100%;
    height:15vh;
    display:flex;
    flex-direction: column;
    border:1px solid #ececec;
}

.line-one {
    display:flex;
    flex-direction: row;
    justify-content: space-between;
    width:100%;
    height:20%;
    align-items: center;
    gap:.5vw;
    font-family:Golos-Text;
}

.box-position {
    display:flex;
    flex-direction: row;
    justify-content: start;
    width:100%;
    height:20%;
    align-items: start;
    gap:.5vw;
    font-family:Golos-Text;
}

.box-id {
    margin-left:1vw;
    color:#aaaaaa;
}

.line-group {
    display:flex;
    flex-direction: row;
    width: 40%;
    height:100%;
    justify-content: end;
    align-items: center;
    gap:1vw;
}

.box-status {
    background-color: #64f802;
    color:#fff;
    display:flex;
    justify-content: center;
    align-items: center;
    height:90%;
    padding: 0 1vw;
    margin-right: 1vw;
}

.box-name-sport {
    margin-left:1vw;
    width:50%;
    overflow:hidden;
    white-space: nowrap;
    font-weight: 600;
}
.box-name-champ {
    margin-right:1vw;
    width:50%;
    overflow:hidden;
    white-space: nowrap;
    display: flex;
    justify-content: end;
    font-weight: 600;
}

.box-descriptions {
    width:100%;
    overflow:hidden;
    white-space: nowrap;
    margin-left:1vw;
    color:#aaaaaa;
    display:flex;
    flex-direction: row;
    gap: .7vw;
}

.box-age-groups {
    gap: .7vw;
    width:100%;
    overflow:hidden;
    white-space: nowrap;
    margin-left:1vw;
    color:#909090;
    display:flex;
    flex-direction: row;
}

.box-country {
    margin-left:1vw;
    width:10%;
}

.box-subjetc {
    width:30%;
}

.box-city {
    width:30%;
}
.box-count {
    width:26%;
    display:flex;
    justify-content: end;
    align-items: center;
    color:#949494;
}
</style>