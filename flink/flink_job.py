from pyflink.datastream import StreamExecutionEnvironment
import json

env = StreamExecutionEnvironment.get_execution_environment()

def process(record):
    data = json.loads(record)
    risk_score = (
        0.3 * data['heart_rate'] +
        0.3 * (100 - data['spo2']) +
        0.2 * data['resp_rate']
    )
    data['risk_score'] = risk_score
    return json.dumps(data)

ds = env.socket_text_stream("localhost", 9999)

processed = ds.map(process)

processed.print()

env.execute("ICU Monitoring Job")