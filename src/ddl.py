from sqlalchemy import DDL

firebase_send_notification = DDL('''\
create extension if not exists pg_net;
create or replace function firebase_send_notification()
returns trigger
language plpgsql
as $$
begin
    perform net.http_post(
        url := 'https://sendnotifications.run.app',
        body := jsonb_build_object('type', TG_OP, 'table', TG_TABLE_NAME, 'record', row_to_json(new), 'schema', TG_TABLE_SCHEMA),
        headers := '{"Content-Type": "application/json"}'::jsonb,
        timeout_milliseconds := 5000
    );
    return new;
end;
$$;

drop trigger if exists "firebase-send-notification-webhook" on messages;
create trigger "firebase-send-notification-webhook"
after insert on messages
for each row
execute function firebase_send_notification();''')
