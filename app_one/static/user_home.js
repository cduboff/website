<script>
    {$("#more_info").click(function (event) {
        console.log("clicked on link")
        console.log("submitting request")
        var recipe_id = (document.getElementById('recipe.id').textContent);
        $.ajax({
            url: '/find_recipe/' + recipe_id,
            method: 'GET'
        }).done(function (response) {
            console.log(response)
            $('#search_results').html(response)
        });
        return false
    });
</script>