<script>
export default {
  props: {
    questionnaire: Object
  },
  data() {
    return {
      nomQuestionnaire: ""
    };
  },
  methods: {
    modifierQuestionnaire(args) {
      let questionnaireUri = args.uri;
      let nomQuestionnaire = args.nomQuestionnaire;
      let sent = { "name": nomQuestionnaire };
      let response = fetch(questionnaireUri, { headers: { "Content-Type": "application/json" }, method: "PUT", body: JSON.stringify(sent) });
      response.then(
        result => result.json()
      ).then(
        result => {
          let resultQuestionnaire = result["questionnaire"];
          this.questionnaires = this.questionnaires.map(questionnaire => questionnaire.uri === resultQuestionnaire.uri ? resultQuestionnaire : questionnaire);
        }
      ).catch(error => console.log(error));
    }
</script>