<template>
    <div class="main-box">
        <div class="label-info">Министерство</div>
        <div class="info-box">
            <div class="info-box-left">
                
                <div class="text-info-box">
                    Министерство спорта Российской Федерации (Минспорт России) является федеральным органом исполнительной власти, осуществляющим функции по выработке и реализации государственной политики и нормативно-правовому регулированию в сфере физической культуры и спорта, а также по оказанию государственных услуг (включая предотвращение допинга в спорте и борьбу с ним) и управлению государственным имуществом в сфере физической культуры и спорта.
                </div>
            </div>
            <div class="info-box-right"></div>
            
        </div>
        <div class="brass-box">
            <div class="label-brass">Руководство министерства</div>
            <div class="minister-box">
                <div class="photo-box">
                    <img src="../assets/Degtyrov.JPG">
                </div>
                <div class="content-box">
                    <div class="name-line" id="content-line">Дегтярев Михаил Владимирович</div>
                    <div class="post-line" id="content-line">Министр спорта</div>
                </div>
            </div>
            <div class="deputy-ministers-box">
                <div class="line-one">
                    <div class="deputy">
                        <div class="photo-box-2">
                            <img src="../assets/Baisultanov.JPG">
                        </div>
                        <div class="content-box">
                            <div class="name-line-2" id="content-line-2">Байсултанов Одес Хасаевич</div>
                            <div class="post-line-2" id="content-line-2">Первый заместитель Министр</div>
                        </div>
                    </div>
                    <div class="deputy">
                        <div class="photo-box-2">
                            <img src="../assets/Nikitin.JPG">
                        </div>
                        <div class="content-box">
                            <div class="name-line-2" id="content-line-2">Никитин Александр Александрович</div>
                            <div class="post-line-2" id="content-line-2">Статс-секретарь - заместитель Министра</div>
                        </div>
                    </div>
                </div>
                <div class="line-two">
                    <div class="deputy">
                        <div class="photo-box-2">
                            <img src="../assets/Gandilyan.JPG">
                        </div>
                        <div class="content-box">
                            <div class="name-line-2" id="content-line">Гандилян Мгер Миранович</div>
                            <div class="post-line-2" id="content-line">Заместитель Министра</div>
                        </div>
                    </div>
                    <div class="deputy">
                        <div class="photo-box-2">
                            <img src="../assets/Morozov.JPG">
                        </div>
                        <div class="content-box">
                            <div class="name-line-2" id="content-line">Морозов Алексей Алексеевич</div>
                            <div class="post-line-2" id="content-line">Заместитель Министра</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.main-box {
    width:100%;
    height:100%;
    display: flex;
    justify-content: start;
    align-items: center;
    flex-direction: column;
}
.info-box {
    width: 85%;
    height:25%;
    display:flex;
    flex-direction: row;
    justify-content: center;
    align-items: start;
    margin-top:2vh;
}
.brass-box {
    width:90%;
    height:40%;
    display:flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    gap:1vh;
    margin-top:6vh;
}

.label-brass {
    font-family: Golos-Text-Semibold;
    font-size:4vh;
    width:100%;
    padding-left:8vw;
}

.label-info {
    font-family: Golos-Text-Semibold;
    font-size:4vh;
    width:90%;
    padding-left:8vw;
}

.minister-box {
    display:flex;
    flex-direction: row;
    background-color: #fff;
    width:90%;
    height:25%;
    border-radius: 1vw;
    border:1px solid #e6e6e6;
    margin-top:2vh;
}

.photo-box {
    width:10%;
    height:100%;
    display: flex;
    justify-content: center;
    align-items: center;
    
}

.photo-box img {
    width:60px;
    height: 60px;
    border-radius: 50%;
}

.content-box {
    width:90%;
    display: flex;
    flex-direction: column;
    padding-top:1vh;
}

#content-line {
    height:40%;
    width:100%;
    display: flex;
    justify-content: start;
    align-items: center;
}

.name-line {
    font-family: Golos-Text-Semibold;
    font-size:2vh;
}

.post-line {
    font-family: Golos-Text;
    color:#a9a9a9;
}

.deputy-ministers-box {
    display:flex;
    flex-direction: column;
    width:90%;
    height:40%;
    border-radius: 1vw;
    gap:1vh;
}

.line-one {
    display: flex;
    flex-direction: row;
    width:100%;
    height:50%;
    border-radius: 1vw;
    justify-content: space-between;
    gap:.5vw;
}

.line-two {
    display: flex;
    flex-direction: row;
    width:100%;
    height:50%;
    border-radius: 1vw;
    justify-content: space-between;
    gap:.5vw;
}

.deputy {
    width:50%;
    height:100%;
    display:flex;
    flex-direction: row;
    border-radius: 1vw;
    background-color: #fff;
    border:1px solid #e6e6e6;
}

.photo-box-2 {
    width:22%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.photo-box-2 img {
    width:60px;
    height: 60px;
    border-radius: 50%;
}

.content-box-2 {
    width:90%;
    display: flex;
    flex-direction: column;
    padding-top:1vh;
}

#content-line-2 {
    height:40%;
    width:100%;
    display: flex;
    justify-content: start;
    align-items: center;
}

.name-line-2 {
    font-family: Golos-Text-Semibold;
    font-size:1.8vh;
}

.post-line-2 {
    font-family: Golos-Text;
    color:#a9a9a9;
}

.info-box-left {
    width:60%;
    height:100%;
}

.info-box-right {
    width:35%;
    height:100%;
    background: url('../assets/Zdanie-minsport.JPG');
    background-size:cover;
    background-repeat: no-repeat;
    background-position-y: 40%;
}

.text-info-box {
    font-family: Golos-text;
    text-align: justify;
    padding:0 1vw 1vw 0;
    font-size: 1.9vh;
}
</style>