<template lang="html">
    <div class="">
        <h1>Ciao, Componente Esempio!</h1>
        <h2> {{message}}</h2>
    </div>
</template>
<script>
export default {
    data() {
        return {
            message:"Ciao a tutti"
        }
    }
}
</script>
<style lang="css">
    h2 {
        color: red;
    }
</style>