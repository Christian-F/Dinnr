<template>
    <div>
        {{ name }}
    </div>
</template>

<script>
    export default {
        name: "FoodItem",
        props: {
            name: {
                type: String,
                required: true,
            },
            brand_name: {
                type: String,
                required: true,
            },
        },
    }
</script>

<style scoped>
    div {
        display: flex;
        width: 400px;
        min-height: 100px;
        padding: 10px;
        background-color: rgb(137, 187, 243);
        border: none;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.4);
        border-radius: 5px;
        font-family: Avenir, Helvetica, Arial, sans-serif;
        font-size: 1em;
        margin: 5px;
    }
</style>
